dist_sbin_SCRIPTS = simta-mscan

EXTRA_DIST = VERSION packaging/rpm/simta-mscan.spec

rpm: dist-xz
	rpmbuild -ta $(distdir).tar.xz
