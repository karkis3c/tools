## Hello Eveyone, this is a very old project. It is an executable program written in Go, but I do not have the Go source code for this program. It is a static binary program.

Tool to create instant encoded payloads to bypass filters

## Install

1. `wget `
2. `chmod +x kakxencoder;sudo mv kakxencoder /usr/local/bin`

Help menu

```
-u (URL encode)
-b (base64 encode)
-d (decode)
-all (encode/decode all levels from 1 up to the specified level)
```

Usage:

`kakxencoder -u int`

## Examples

```
~$ echo '<script>alert(1)</script>' | kakxencoder -b 1
PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==
```
```
~$ echo '<script>alert(1)</script>' | kakxencoder -b 3 -all
PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==
UEhOamNtbHdkRDVoYkdWeWRDZ3hLVHd2YzJOeWFYQjBQZz09
VUVoT2FtTnRiSGRrUkRWb1lrZFdlV1JEWjNoTFZIZDJZekpPZVdGWVFqQlFaejA5
```
```
~$ echo '<script>alert(1)</script>' | kakxencoder -u 1
%3Cscript%3Ealert%281%29%3C%2Fscript%3E
```
```
~$ echo '<script>alert(1)</script>' | kakxencoder -u 3 -all
%3Cscript%3Ealert%281%29%3C%2Fscript%3E
%253Cscript%253Ealert%25281%2529%253C%252Fscript%253E
%25253Cscript%25253Ealert%2525281%252529%25253C%25252Fscript%25253E
```
```
echo '../../etc/passwd' | kakxencoder -u 1
echo '../../etc/passwd' | kakxencoder -u 1 | kakxencoder -u 1 -d
cat xss_payloads.txt | kakxencoder -u 3 -all > uencoded.txt
cat xss_payloads.txt | kakxencoder -b 2 -all > bencoded.txt
```
