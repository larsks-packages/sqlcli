%if 0%{?rhel} && 0%{?rhel} <= 5
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

Name:		sqlcli
Version:	1
Release:	1%{?dist}
Summary:	A SQL query utility.

License:	GPL
URL:		http://github.com/larsks/sqlcli/
Source0:	https://github.com/larsks/sqlcli/archive/%{name}-%{version}.tar.gz

BuildRequires:	python
BuildRequires:	python-setuptools
Requires:	python
Requires:	python-prettytable
Requires:	python-sqlalchemy

%description
This is a tool that uses SQLAlchemy to execute SQL queries against a SQL
database specified via a URL or an INI-style file.

%prep
%setup -q -n %{name}-%{name}-%{version}

%install
> requirements.txt
python setup.py install --root=$RPM_BUILD_ROOT

%files
%doc README.md

%{python_sitelib}/sqlcli-1-py*.egg-info
%{python_sitelib}/sqlcli/__init__.py
%{python_sitelib}/sqlcli/__init__.pyc
%{python_sitelib}/sqlcli/__init__.pyo
%{python_sitelib}/sqlcli/main.py
%{python_sitelib}/sqlcli/main.pyc
%{python_sitelib}/sqlcli/main.pyo

%{_bindir}/sqlcli

%changelog

* Mon Nov 25 2013 Lars Kellogg-Stedman <lars@oddbit.com> - 1-1
- initial packaging

