from django.conf import settings
your_media_root = settings.MEDIA_URL
import pandas as pd
def showimage(request, file_name):
    import random
    import django
    import datetime

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter
    gg = pd.read_csv(your_media_root + file_name, header=None).as_matrix()
    fig = Figure(facecolor="white")
    ax = fig.add_subplot(111)
    x = []
    y = []
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=1)
    for i in gg:
        x.append(now)
        now += delta
        y.append(i[1:])
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas = FigureCanvas(fig)
    response = django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)

    return response