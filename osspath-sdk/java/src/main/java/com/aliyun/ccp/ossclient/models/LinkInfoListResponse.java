// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ccp.ossclient.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class LinkInfoListResponse extends TeaModel {
    @NameInMap("items")
    @Validation(required = true)
    public java.util.List<LinkInfoResponse> items;

    public static LinkInfoListResponse build(java.util.Map<String, ?> map) throws Exception {
        LinkInfoListResponse self = new LinkInfoListResponse();
        return TeaModel.build(map, self);
    }

}
