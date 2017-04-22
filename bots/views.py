from __future__ import absolute_import
from __future__ import division, print_function

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

import requests
from bs4 import BeautifulSoup
import os

def url(request):
	if(request.GET.get('url','url') != 'url'):
		url = request.GET.get('url','url')
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
	elif(request.GET.get('image','image')):
		r = requests.get(request.GET.get('image'))
		test = request.GET.get('image').split("/")
		urlval = str(''.join(test[:3]))
		data = r.text
		soup = BeautifulSoup(data, "lxml")
		temp = []
		for link in soup.find_all('img'):
			image = link.get("src")
			temp.append(image)
		for loc,i in enumerate(temp):
			if(i[0] == "/"):
				temp[loc] =   urlval + temp[loc]
		return JsonResponse({"images" : '  '.join(temp)})	
	 
	