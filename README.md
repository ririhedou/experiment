# experiment

## Result for 1 subfolder
ls -v /mnt/sdb1/domcrawl/htmls/1/ | grep -n "undroider"       ketian@ketian

31052:undroider.com

/tmp/1 » ls | wc -l                                               ketian@ketian
519

I name it as domainName-index

An example of ipfw.edu-9                                        
https://4352641.fls.doubleclick.net/activityi;src=4352641;type=ip1460;cat=homep0;ord=4989106578296.634?%

## Results for Iframe and iframe 2

Iframe folder: 
```
total urls:4814
unique urls: 291
```

Iframe2 folder:
```
total urls: 7949
unique urls: 304
```

## Result for Force Execution
### Step 1: using jalangi2 if condition instrumentation to see whether it has conditions

### Step 2: instrumentation depends on the if condition results.

--[no condition] if it does not have the condition, not need to instrument again, just append my mutation observer code to the original iframe-injection script code.

--[has condition] if it has conditions, we instrumented this html multiple times with different if-condition configurations, 
We append my mutation observer code to the instrumented code

### Step 3:simulate and detect iframe injection

### Tested Examples

tested HTMLs are here: https://github.com/ririhedou/experiment/tree/master/ex_aug_23

we do not detect condition, directly use mutationObserevr
```python
python if_force_execution.py ~/Desktop/jsiframe/jalangi2/kt_test/ke_benchs/iframe.html
original condition{}
we direct run without instrumentation
detect an iframe injection: src->https://www.w3schools.com/
```

We have condition 
```python
python if_force_execution.py ~/Desktop/jsiframe/jalangi2/kt_test/ke_benchs/if_bomb.html
original condition{8: 0}
We force execute this condition:dictionary = {8:false};
We force execute this condition:dictionary = {8:true};
detect an iframe injection: src->https://www.w3schools.com/jsref/met_doc_write.asp
```
the if_bomb.html is at aug_23




## Result for using mutation observer

https://hacks.mozilla.org/2012/05/dom-mutationobserver-reacting-to-dom-changes-without-killing-browser-performance/

sample.html: my test for mutation observers

sshot: screenshot.png for sample.html

the last one: I insert my code after instrumentation


I also tested M's data:

https://gist.github.com/ririhedou/52f8ed746af03979d09d3794c1f8b898

It detects the iframe injection:

[mutationObserve][ketian][iframe][summary]src->http://licfetirjglfwpfg.pro/in.cgi?14


## Crawling data

https://gist.github.com/ririhedou/c51f86f8a164326569ba40bc5d2660bb

current 8 fodlers 100,000*8 = 800,000
