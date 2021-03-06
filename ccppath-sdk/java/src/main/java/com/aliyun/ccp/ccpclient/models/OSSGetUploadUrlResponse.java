// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ccp.ccpclient.models;

import com.aliyun.tea.*;

/**
 * Get UploadUrl Response
 */
public class OSSGetUploadUrlResponse extends TeaModel {
    @NameInMap("create_at")
    public String createAt;

    @NameInMap("domain_id")
    @Validation(pattern = "[a-z0-9A-Z]+")
    public String domainId;

    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    @NameInMap("file_path")
    public String filePath;

    @NameInMap("part_info_list")
    public java.util.List<UploadPartInfo> partInfoList;

    @NameInMap("upload_id")
    public String uploadId;

    public static OSSGetUploadUrlResponse build(java.util.Map<String, ?> map) throws Exception {
        OSSGetUploadUrlResponse self = new OSSGetUploadUrlResponse();
        return TeaModel.build(map, self);
    }

}
