# coding-exercises
Short coding exercises 

### Exercise 2

Example input:
```
{
  "pkg1": ["pkg2", "pkg3"],
  "pkg2": ["pkg3"],
  "pkg3": []
}
```
Output for said example:
```
- pkg1
  - pkg2
    - pkg3
  - pkg3
- pkg2
  - pkg3
- pkg3
```
