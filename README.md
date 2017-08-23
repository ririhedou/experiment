# experiment

temporaryFiles

## Result for Force Excution
```python
python if_force_execution.py ~/Desktop/jsiframe/jalangi2/kt_test/ke_benchs/if_bomb.html
original condition{8: 0}
We force execute this condition:dictionary = {8:false};
We force execute this condition:dictionary = {8:true};
detect an iframe injection: src->https://www.w3schools.com/jsref/met_doc_write.asp
```
the if_bomb.html is at aug_23

## Result for using mutationObserver

https://hacks.mozilla.org/2012/05/dom-mutationobserver-reacting-to-dom-changes-without-killing-browser-performance/

sample.html: my test for mutationObserver

sshot: screenshot.png for sample.html

the last one: i insert my code after instrumentation


I also tested M's data:

https://gist.github.com/ririhedou/52f8ed746af03979d09d3794c1f8b898

It detects the iframe injection:

[mutationObserve][ketian][iframe][summary]src->http://licfetirjglfwpfg.pro/in.cgi?14


## Crawling data

https://gist.github.com/ririhedou/c51f86f8a164326569ba40bc5d2660bb

current 6 fodlers 10,000*6 = 60,000
