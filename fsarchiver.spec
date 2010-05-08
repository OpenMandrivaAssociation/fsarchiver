Name:		fsarchiver
Version:	0.6.8
Release:	%mkrel 2

Summary:	Safe and flexible file-system backup/deployment tool
Group:		Archiving/Backup
License:	GPLv2
URL:		http://www.fsarchiver.org
Source0:  	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz      
# all patches from upstream: http://patches.fsarchiver.org/
Patch0:		fsarchiver-0.6.8-01-probe-lvm.patch
Patch1:		fsarchiver-0.6.8-02-fix-rest-small-archives.patch
Patch2:		fsarchiver-0.6.8-03-restore-error-handling.patch
Patch3:		fsarchiver-0.6.8-04-remove-all-volumes-on-error.patch
Patch4:		fsarchiver-0.6.8-05-fix-ntfs-links.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	e2fsprogs-devel => 1.41.4
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
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README THANKS NEWS ChangeLog
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}*
