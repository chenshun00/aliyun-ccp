// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ccp.ccpclient.models;

import com.aliyun.tea.*;

/**
 * List my drive request
 */
public class ListMyDriveRequest extends TeaModel {
    @NameInMap("limit")
    public Integer limit;

    @NameInMap("marker")
    public String marker;

    public static ListMyDriveRequest build(java.util.Map<String, ?> map) throws Exception {
        ListMyDriveRequest self = new ListMyDriveRequest();
        return TeaModel.build(map, self);
    }

}
