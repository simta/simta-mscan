dist_sbin_SCRIPTS = simta-mscan

EXTRA_DIST = packaging/rpm/simta-mscan.spec

rpm: dist-gzip
	rpmbuild -ta $(distdir).tar.gz
