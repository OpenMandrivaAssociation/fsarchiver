Name:		fsarchiver
Version:	0.6.17
Release:	1

Summary:	Safe and flexible file-system backup/deployment tool
Group:		Archiving/Backup
License:	GPLv2
URL:		http://www.fsarchiver.org
Source0:  	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz      
Patch0:		fsarchiver-0.6.13-linking.patch
BuildRequires:	pkgconfig(ext2fs)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(blkid)
BuildRequires:	e2fsprogs
BuildRequires:	attr-devel
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	bzip2-devel
BuildRequires:	liblzo-devel
BuildRequires:	pkgconfig(liblzma)

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
sed -i -e 's/^\([a-z]*_CFLAGS.*\)-ggdb/\1/' src/Makefile.am
%configure2_5x

%make V=1

%install
%makeinstall_std

%files
%doc README THANKS NEWS ChangeLog
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}*
