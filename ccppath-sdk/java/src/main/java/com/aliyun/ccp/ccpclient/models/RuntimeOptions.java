// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ccp.ccpclient.models;

import com.aliyun.tea.*;

public class RuntimeOptions extends TeaModel {
    @NameInMap("autoretry")
    public Boolean autoretry;

    @NameInMap("ignoreSSL")
    public Boolean ignoreSSL;

    @NameInMap("maxAttempts")
    public Integer maxAttempts;

    @NameInMap("backoffPolicy")
    public String backoffPolicy;

    @NameInMap("backoffPeriod")
    public Integer backoffPeriod;

    @NameInMap("readTimeout")
    public Integer readTimeout;

    @NameInMap("connectTimeout")
    public Integer connectTimeout;

    @NameInMap("httpProxy")
    public String httpProxy;

    @NameInMap("httpsProxy")
    public String httpsProxy;

    @NameInMap("noProxy")
    public String noProxy;

    @NameInMap("maxIdleConns")
    public Integer maxIdleConns;

    @NameInMap("localAddr")
    public String localAddr;

    @NameInMap("socks5Proxy")
    public String socks5Proxy;

    @NameInMap("socks5NetWork")
    public String socks5NetWork;

    public static RuntimeOptions build(java.util.Map<String, ?> map) throws Exception {
        RuntimeOptions self = new RuntimeOptions();
        return TeaModel.build(map, self);
    }

}
