from random import randint

from django.db.models import F
from django.shortcuts import render
from ipware import get_client_ip

from game.models import Politician, GameOverStatistics
from game.utils import try_parse_int


def index(request):
    client_ip, _ = get_client_ip(request)
    user_agent = request.META.get('HTTP_USER_AGENT')

    lost = False
    answered_politician_ids = []
    correct_politician = None
    politicians = Politician.objects.all()
    if request.method == 'POST':
        answered_politician_ids = request.POST.get('answered_politician_ids', '') or ''
        answered_politician_ids = list([try_parse_int(i) for i in answered_politician_ids.strip().split(',') if
                                        try_parse_int(i) is not None])
        correct_id = request.POST.get('correct_id')
        selected_id = request.POST.get('selected_id')

        if correct_id != selected_id or Politician.objects.count() - len(answered_politician_ids) <= 1:
            lost = True
            politicians = politicians.filter(id__in=[correct_id, selected_id])
            correct_politician = Politician.objects.filter(id=correct_id).first()
            selected_politician = Politician.objects.filter(id=selected_id).first()

            game_over = GameOverStatistics()
            game_over.correct_politician = correct_politician
            game_over.selected_politician = selected_politician
            game_over.user_ip = client_ip
            game_over.user_agent = user_agent
            game_over.correct_count = len(answered_politician_ids)
            game_over.save()
        else:
            answered_politician_ids.append(selected_id)
            politicians = politicians.exclude(id__in=answered_politician_ids)

    gender_order = F('is_male').asc() if randint(0, 10) < 3 else F('is_male').desc()
    politicians = list(politicians.order_by(gender_order, '?')[:2])
    correct_potician_position = randint(0, 1)

    correct_politician = correct_politician if correct_politician else politicians[correct_potician_position]
    return render(request, 'web/index.html',
                  {'correct_politician': correct_politician, 'politicians': politicians,
                   'answered_ids': answered_politician_ids,
                   'lost': lost})
