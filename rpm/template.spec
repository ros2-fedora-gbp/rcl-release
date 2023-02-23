%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-rcl-yaml-param-parser
Version:        5.8.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rcl_yaml_param_parser package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       libyaml-devel
Requires:       ros-rolling-libyaml-vendor
Requires:       ros-rolling-rcutils
Requires:       ros-rolling-rmw
Requires:       ros-rolling-ros-workspace
BuildRequires:  libyaml-devel
BuildRequires:  ros-rolling-ament-cmake-ros
BuildRequires:  ros-rolling-libyaml-vendor
BuildRequires:  ros-rolling-rcutils
BuildRequires:  ros-rolling-rmw
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-rolling-ament-cmake-gtest
BuildRequires:  ros-rolling-ament-lint-auto
BuildRequires:  ros-rolling-ament-lint-common
BuildRequires:  ros-rolling-mimick-vendor
BuildRequires:  ros-rolling-osrf-testing-tools-cpp
BuildRequires:  ros-rolling-performance-test-fixture
BuildRequires:  ros-rolling-rcpputils
%endif

%description
Parse a YAML parameter file and populate the C data structure.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/rolling" \
    -DAMENT_PREFIX_PATH="/opt/ros/rolling" \
    -DCMAKE_PREFIX_PATH="/opt/ros/rolling" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Thu Feb 23 2023 Audrow Nash <audrow@openrobotics.org> - 5.8.0-1
- Autogenerated by Bloom

* Mon Feb 13 2023 Audrow Nash <audrow@openrobotics.org> - 5.7.0-1
- Autogenerated by Bloom

* Mon Dec 05 2022 Audrow Nash <audrow@openrobotics.org> - 5.6.0-1
- Autogenerated by Bloom

* Wed Nov 02 2022 Ivan Paunovic <ivanpauno@ekumenlabs.com> - 5.5.0-1
- Autogenerated by Bloom

* Tue Sep 13 2022 Ivan Paunovic <ivanpauno@ekumenlabs.com> - 5.4.1-1
- Autogenerated by Bloom

* Fri Apr 29 2022 Ivan Paunovic <ivanpauno@ekumenlabs.com> - 5.4.0-1
- Autogenerated by Bloom

* Tue Apr 26 2022 Ivan Paunovic <ivanpauno@ekumenlabs.com> - 5.3.1-1
- Autogenerated by Bloom

* Tue Apr 05 2022 Ivan Paunovic <ivanpauno@ekumenlabs.com> - 5.3.0-1
- Autogenerated by Bloom

* Thu Mar 31 2022 Ivan Paunovic <ivanpauno@ekumenlabs.com> - 5.2.1-1
- Autogenerated by Bloom

* Thu Mar 24 2022 Ivan Paunovic <ivanpauno@ekumenlabs.com> - 5.2.0-1
- Autogenerated by Bloom

* Tue Mar 01 2022 Ivan Paunovic <ivanpauno@ekumenlabs.com> - 5.1.0-1
- Autogenerated by Bloom

* Tue Feb 08 2022 Ivan Paunovic <ivanpauno@ekumenlabs.com> - 5.0.1-2
- Autogenerated by Bloom

