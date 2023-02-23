# DefaultKeyTester

This python code makes all the possible default credentials of the vendor registered.

## Usage
``` python
    python3 ./main.py <vendor>
```
You need to put one of the vendors in the vendor scope.

If you want to see ALL the possible vendors you can do this code :
``` python
    python3 ./main.py ALL
```

## Example
```
    python3 ./main.py apc   

                For the user apc

        - apc:apc

                For the user device

        - device:apc
```
And yes, it's Case Sensitive.
