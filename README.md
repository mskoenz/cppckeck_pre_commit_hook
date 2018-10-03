# cppcheck hook for pre-commit

[cppcheck](https://github.com/danmar/cppcheck/) package for [pre-commit](http://pre-commit.com).

I selected all possible checks short of unusedFunction which might be too severe for some. Just modify the args line below.

## Using cppcheck with pre-commit

```yaml
-   repo: git://github.com/mskoenz/pre-commit-cppcheck
    sha: master
    hooks:
    -   id: cppcheck
        args: [--enable=missingInclude,information,portability,performance,style,warning]
```
