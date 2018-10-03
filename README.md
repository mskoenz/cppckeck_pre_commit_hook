# cppcheck hook for pre-commit

[cppcheck](https://github.com/danmar/cppcheck/) package for [pre-commit](http://pre-commit.com).

I needed to write a wrapper around cppcheck, since it can only exit with non-zero on errors. But I wanted other warnings to also abort the commit.
This wrapper only exposes a limited part of the cppcheck-interface, namely:

```
--enable  (default: all)
--std     (default: c++14)
```

## Using cppcheck with pre-commit

```yaml
-   repo: git://github.com/mskoenz/pre-commit-cppcheck
    sha: v1.1
    hooks:
    -   id: cppcheck_hook
```
