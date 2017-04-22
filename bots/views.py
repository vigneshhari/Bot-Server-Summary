from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Max
from django.http import HttpResponseRedirect


from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


def url(request):
	url = request.GET.get('url')
	print(url)
	LANGUAGE = "english"
	SENTENCES_COUNT = 5
	out=[]
	parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
	stemmer = Stemmer(LANGUAGE)
	summarizer = Summarizer(stemmer)
	summarizer.stop_words = get_stop_words(LANGUAGE)
	for sentence in summarizer(parser.document, SENTENCES_COUNT):
	    out.append(str(sentence))
	return JsonResponse({'content' : str("\n".join(out)) })
