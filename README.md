# simta-mscan

`simta-mscan` is the reference implementation of a content filter
for the [simta](https://github.com/simta/simta/) MTA. Details
on the content filter interface used by simta can be found
[here](https://github.com/simta/simta/blob/main/doc/content_filter.md).

`simta-mscan` is a POSIX-compliant shell script
that is designed to run under the [Debian Almquist
shell](https://git.kernel.org/pub/scm/utils/dash/dash.git/). The
script does not actually do any filtering itself, it sources
individual filters (which must also be written in POSIX-compliant
shell) from `/etc/mail/filters`. These filters must be marked as
executable and will be run in lexicographic order.

## Filter example

```sh
#!/bin/dash

from_domain=${SIMTA_SMTP_MAIL_FROM##*@}
if [ "x$from_domain" = 'xexample.com' ] || [ "x${from_domain#*.}" = 'xexample.com' ]; then
    log "10_testfilter: matched domain $from_domain"
    filter_exit $MESSAGE_TEMPFAIL
fi

if check_tfile; then
    fgrep -q 'XJS*C4JDBQADN1.NSBN3*2IDNEN*GTUBE-STANDARD-ANTI-UBE-TEST-EMAIL*C.34X' $SIMTA_TFILE
    if [ $? -eq 0 ]; then
        log "10_testfilter: found GTUBE"
        filter_exit $MESSAGE_REJECT
    fi
fi
```
