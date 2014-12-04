Summary: My app 
Name: hello
Version: 0.0.1
Release: 1
License: GPL+
Group: Development/Tools
SOURCE0 : %{name}.tar.gz
URL: http://kevinvanrooijen.com/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: ghc
%description
%{summary}

%prep
%setup -q

%build
# Empty section.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin
make
cp hello %{buildroot}/usr/local/bin

%clean
rm -rf %{buildroot}


%files
/usr/local/bin

%changelog
* Sun Nov 30 2014 Foobar
- First Build

