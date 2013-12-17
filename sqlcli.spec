%if 0%{?rhel} && 0%{?rhel} <= 5
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%if 0%{?rhel} && 0%{?rhel} <= 6
%define python %{__python}
%else
%define python %{__python2}
%endif

Name:		sqlcli
Version:	2
Release:	3%{?dist}
Summary:	A command-line SQL query utility

License:	GPLv3+
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
%{python} setup.py build

%install
> requirements.txt
%{python} setup.py install --prefix=%{_prefix} --root=%{buildroot} -O1 --skip-build

%files
%doc README.md COPYING

%attr(0755,root,root) %{_bindir}/sqlcli

%{python_sitelib}/sqlcli-1-py*.egg-info
%{python_sitelib}/sqlcli

%changelog

* Wed Nov 27 2013 Lars Kellogg-Stedman <lars@oddbit.com> - 2-3
- update license name (GPLv3 -> GPLv3+)
- added license file to %doc

* Mon Nov 25 2013 Lars Kellogg-Stedman <lars@oddbit.com> - 2-2
- udpated sqlcli upstream includes license information
- spec file fixes in response to package review

* Mon Nov 25 2013 Lars Kellogg-Stedman <lars@oddbit.com> - 1-1
- initial packaging

