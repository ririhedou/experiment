# experiment

temporary files

## Result for Force Execution
### Step 1: using jalangi2 if condition instrumentation to see whether it has conditions

### Step 2: instrumentation depends on the if condition.

--[no condition] if it does not have the condition, not need to instrument again, just append my mutation observer code to the original iframe-injection script code.

--[has condition] if it has conditions, we instrumented this html multiple times with different if-condition configurations, 
We append my mutation observer code to the instrumented code

### Step 3:simulate and detection iframe injection

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

current 6 fodlers 10,000*6 = 60,000
