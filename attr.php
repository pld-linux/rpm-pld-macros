%__php_provides		%{_rpmhome}/php.prov
# define 'php_req_new' in ~/.rpmmacros to use php version of req finder
%__php_requires		env PHP_MIN_VERSION=%{?php_min_version} %{_rpmhome}/php.req%{?php_req_new:.php}
%__php_magic		^PHP script.*
%__php_path		\\.php$
