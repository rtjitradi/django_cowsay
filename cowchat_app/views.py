from django.shortcuts import render
from cowchat_app.models import TextLine
from cowchat_app.forms import TextlineForm
import subprocess


# has a view for the index that does two things: if there is output, render it to the browser, and always renders a fresh version of our form
# on submission of the form, uses python's `subprocess (Links to an external site.)Links to an external site.` module to pass the submitted text to the cowsay utility and retrieves the output
# re-renders the homepage with a fresh form and the output from cowsay (hint: the output is preformatted)
# has a page at the endpoint /history that displays the 10 most recent strings submitted
# # Create your views here.


def textline_view(request):
    if request.method == "POST":
        textline_form = TextlineForm(request.POST)
        if textline_form.is_valid():
            textline_data = textline_form.cleaned_data
            cowsay_data = textline_data('text_line')
            TextLine.objects.create(text_line=textline_data.get('text_line'))
# Refer to subprocess doc and Corey' https://www.youtube.com/watch?v=2Fp1N6dof0Y&t=932s
        cowsay_outputs = subprocess.run(['cowsay', cowsay_data], capture_output=True, text=True)
        print(cowsay_outputs.stdout)
        return render(request, 'index.html', {"textline_form": TextlineForm(), 'cowsay_outputs': cowsay_outputs.stdout})

    textline_form = TextlineForm()
    return render(request, 'index.html', {'textline_form': textline_form})


def lastten_view(request):
    last_ten = TextLine.objects.filter().order_by('-id')[:10]
    return render(request, 'lastten.html', {'last_ten': last_ten})
