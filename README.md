# student-supervisor

Proof of concept to allocate students to supervisor based upon their preferences.

Requires 2 input csvs
* Student preferences with columns
  * name - The students name 
  * n additional columns with their n top preferences
* Supervisor capacity with columns
  * name - the supervisors name
  * capacity - the number of students they can supervise

-----

## Running

Only exposed this to a test for the time being as just to illustrate

```console
hatch run test
```

## License

`student-supervisor` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
