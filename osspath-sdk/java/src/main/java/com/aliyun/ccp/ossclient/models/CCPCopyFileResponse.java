// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ccp.ossclient.models;

import com.aliyun.tea.*;

/**
 * 文件拷贝 response
 */
public class CCPCopyFileResponse extends TeaModel {
    @NameInMap("async_task_id")
    public String asyncTaskId;

    @NameInMap("domain_id")
    @Validation(pattern = "[a-z0-9A-Z]+")
    public String domainId;

    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    @NameInMap("file_id")
    @Validation(pattern = "[a-z0-9]{1,50}")
    public String fileId;

    public static CCPCopyFileResponse build(java.util.Map<String, ?> map) throws Exception {
        CCPCopyFileResponse self = new CCPCopyFileResponse();
        return TeaModel.build(map, self);
    }

}
