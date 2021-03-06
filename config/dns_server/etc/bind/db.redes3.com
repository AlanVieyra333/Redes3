; BIND reverse data file for empty rfc1918 zone
;
; DO NOT EDIT THIS FILE - it is used for multiple zones.
; Instead, copy it, edit named.conf, and use that copy.
;
$TTL	86400
@	IN	SOA	redes3.com. root.redes3.com. (
			      1		; Serial
			 604800		; Refresh
			  86400		; Retry
			2419200		; Expire
			  86400 )	; Negative Cache TTL
;
@	IN	NS	redes3.com.
@	IN	A	10.0.100.100
www	IN	A	10.0.1.1
www	IN	A	10.0.1.2
www	IN	A	10.0.2.1
www	IN	A	10.0.2.2
