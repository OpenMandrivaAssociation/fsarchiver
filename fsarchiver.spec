Name:		fsarchiver
Version:	0.6.15
Release:	1

Summary:	Safe and flexible file-system backup/deployment tool
Group:		Archiving/Backup
License:	GPLv2
URL:		http://www.fsarchiver.org
Source0:  	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz      
Patch0:		fsarchiver-0.6.13-linking.patch
BuildRequires:	pkgconfig(ext2fs)
BuildRequires:	libuuid-devel
BuildRequires:	libblkid-devel
BuildRequires:	e2fsprogs
BuildRequires:	libattr-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	zlib-devel
BuildRequires:	bzip2-devel
BuildRequires:	liblzo-devel
BuildRequires:	lzma-devel

%description
FSArchiver is a system tool that allows you to save the contents of a 
file-system to a compressed archive file. The file-system can be restored 
on a partition which has a different size and it can be restored on a 
different file-system. Unlike tar/dar, FSArchiver also creates the 
file-system when it extracts the data to partitions. Everything is 
checksummed in the archive in order to protect the data. If the archive 
is corrupt, you just loose the current file, not the whole archive.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x

%make V=1

%install
%makeinstall_std

%files
%doc README THANKS NEWS ChangeLog
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}*


%changelog
* Mon Jun 04 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.6.15-1
+ Revision: 802187
- version update 0.6.15

* Mon Mar 19 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.6.13-1
+ Revision: 785752
- BR:pkgconfig(ext2fs)
- version update 0.6.13

* Sat Dec 25 2010 Jani Välimaa <wally@mandriva.org> 0.6.12-1mdv2011.0
+ Revision: 624927
- new version 0.6.12
- finally fix overlinking in a pretty way (add P0)
- increase build time verbosity

* Sun Dec 05 2010 Jani Välimaa <wally@mandriva.org> 0.6.11-1mdv2011.0
+ Revision: 609621
- new version 0.6.11
- drop upstream applied patch

* Sat Nov 27 2010 Funda Wang <fwang@mandriva.org> 0.6.10-3mdv2011.0
+ Revision: 601650
- rebuild for new liblzma

* Thu Oct 21 2010 Jani Välimaa <wally@mandriva.org> 0.6.10-2mdv2011.0
+ Revision: 587168
- add update-supported-btrfs-compat-flags.patch from upstream
- fix overlinking

* Sat Jul 10 2010 Jani Välimaa <wally@mandriva.org> 0.6.10-1mdv2011.0
+ Revision: 550072
- new version 0.6.10
- drop upstream applied patches

* Sat May 08 2010 Jani Välimaa <wally@mandriva.org> 0.6.8-2mdv2010.1
+ Revision: 543988
- add patches from upstream:
  * fsarchiver-0.6.8-02-fix-rest-small-archives.patch
  * fsarchiver-0.6.8-03-restore-error-handling.patch
  * fsarchiver-0.6.8-04-remove-all-volumes-on-error.patch
  * fsarchiver-0.6.8-05-fix-ntfs-links.patch

* Wed Apr 07 2010 Jani Välimaa <wally@mandriva.org> 0.6.8-1mdv2010.1
+ Revision: 532852
- initial Mandriva release based on Fedora .spec

