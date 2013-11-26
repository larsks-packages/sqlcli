Name:		sqlcli
Version:	2
Release:	2%{?dist}
Summary:	A command-line SQL query utility

License:	GPLv3
URL:		http://github.com/larsks/sqlcli/
Source0:	https://github.com/larsks/sqlcli/archive/%{name}-%{version}.tar.gz

BuildRequires:	python2-devel
BuildRequires:	python-setuptools
Requires:	python2
Requires:	python-prettytable
Requires:	python-sqlalchemy

Buildarch:	noarch

%description
This is a tool that uses SQLAlchemy to execute SQL queries against a SQL
database specified via a URL or an INI-style file (such as those used by most
of the OpenStack services).

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
%{__python2} setup.py build

%install
> requirements.txt
%{__python2} setup.py install --prefix=%{_prefix} --root=%{buildroot} -O1 --skip-build

%files
%doc README.md

%attr(0755,root,root) %{_bindir}/sqlcli

%{python_sitelib}/sqlcli-1-py*.egg-info
%{python_sitelib}/sqlcli

%changelog

* Mon Nov 25 2013 Lars Kellogg-Stedman <lars@oddbit.com> - 2-2
- udpated sqlcli upstream includes license information
- spec file fixes in response to package review

* Mon Nov 25 2013 Lars Kellogg-Stedman <lars@oddbit.com> - 1-1
- initial packaging

