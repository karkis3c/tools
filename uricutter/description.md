## Details

- Reads URL(s) from standard input.
- Removes query parameters and shortens paths.
- Outputs the unique URLs to the console.

### The idea behind creating this script is to increase the success rate of attacks during scans, ensuring that scanners do not miss any areas.
## Usage
`cat urls. txt | python3 uricutter.py/ echo | python3 uricutter.py`

## Example
`echo 'https://domain.com/admin/manager/index.php?param=1' | python3 uricutter.py`

## Response
```
https://domain.com/admin
https://domain.com/admin/manager
https://domain.com/admin/index.php
```

## How to Use This for Testing

Directly Indexing/ 403 bypass

`echo 'https://domain.com/admin/manager/setting/index.php' | python3 uricutter.py`

```
https://domain.com/admin [200] [Login]
https://domain.com/admin/manager [200] [Index of /]
https://domain.com/admin/setting/manager/index.php [403]
```

Finding Logs and Backup Files

`echo paths.txt | nuclei -duc -t nuclei-templates/http/exposures -et nuclei-templates/http/exposures/tokens -c 35`

Fuzzing
```
https://domain.com/admin/FUZZ
https://domain.com/admin/manager/FUZZ
...
```

Before your testing:

`cat boring_urls.txt | nuclei -duc -t nuclei-templates/`

This approach may not find everything. 

Instead, use:

```
cat boring_urls.txt | grep '\?' | nuclei -duc -t nuclei-templates/ -dast -c 50
cat paths.txt | nuclei -duc -t nuclei-templates/ -c 40
cat paths.txt | nuclei -duc -t nuclei-templates/ -headless -c 35
cat domains.txt | nuclei -duc -tags cves -rl 20 -c 20
```

Don't forget to use your private templates

```cat paths.txt | nuclei -duc -t redirect-via-path.yaml -t xss-via-path.yaml -t lfi-fuzz-path.yaml -t crlf-fuzz-path.yaml etc..```

* Beginners may not be able to understand this, so keep away from these tools :)

Thankyou all!
