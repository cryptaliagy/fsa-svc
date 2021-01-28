# fsa-svc

Project generated with [krait](http://tlia.ca/krait)

Small flask app, wrapping [pyfsa](http://tlia.ca/fsa) to provide the file generation functionality through a web api.

## Calling the API

To generate a graph, send a CSV string (with spaces instead of newlines to separate between the values) in the same form as [fsa-bot](http://tlia.ca/fsa-bot) requires in the json body. This is the only thing you require- but you can also specify a start, end, and engine.

Example payloads:

```json
{'transitions': 'a,x,y b,x,y'}
{
    'transitions': 'a,x,y b,x,y',
    'start': 'x',
    'end': 'y',
    'engine': 'dot'
}
```
