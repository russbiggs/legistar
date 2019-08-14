# Legistar 

A Python 3.7+ wrapper for the [Legistar API](https://webapi.legistar.com/).

Legistar seeks to provide a modern and minimal wrapper for the legistar HTTP API. Includes configurable TTL Cache for all endpoints.

## Example Usage

```sh
>>> from legistar import Legistar 
>>> api = Legistar('cabq')
>>> person = api.person(42)
>>> print(person)
Person(id=42, guid='7301CA84-6144-45B7-85E6-F4A8B717DC15', last_modified_utc=
datetime.datetime(2014, 5, 24, 4, 9, 56, 420000),row_version='AAAAAAAXInE=', 
first_name='Hess', last_name='Yntema', full_name='Hess Yntema', active_flag=1,
used_sponsor_flag=0, address1=None, city1=None, state1=None, zip1=None, phone=
'(505) 768-3100', fax='(505) 768-3227', email='hyntema@cabq.gov', www='http://
www.cabq.gov/council/ccdist6.html', address2=None, city2=None, state2=None, zi
p2=None, phone2=None, fax2=None, email2=None, www2=None)
```



## Contributing

Contributions in the form of issues and pull requests are welcome