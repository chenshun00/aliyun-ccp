// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ccp.ossclient.models;

import com.aliyun.tea.*;

/**
 * Create file response
 */
public class CCPCreateFileResponse extends TeaModel {
    @NameInMap("domain_id")
    @Validation(pattern = "[a-z0-9]{1,50}")
    public String domainId;

    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    @NameInMap("encrypt_mode")
    public String encryptMode;

    @NameInMap("exist")
    public Boolean exist;

    @NameInMap("file_id")
    @Validation(pattern = "[a-z0-9]{1,50}")
    public String fileId;

    @NameInMap("file_name")
    public String fileName;

    @NameInMap("parent_file_id")
    @Validation(pattern = "[a-z0-9]{1,50}")
    public String parentFileId;

    @NameInMap("part_info_list")
    public java.util.List<UploadPartInfo> partInfoList;

    @NameInMap("rapid_upload")
    public Boolean rapidUpload;

    @NameInMap("status")
    public String status;

    @NameInMap("streams_upload_info")
    public java.util.Map<String, ?> streamsUploadInfo;

    @NameInMap("type")
    public String type;

    @NameInMap("upload_id")
    public String uploadId;

    public static CCPCreateFileResponse build(java.util.Map<String, ?> map) throws Exception {
        CCPCreateFileResponse self = new CCPCreateFileResponse();
        return TeaModel.build(map, self);
    }

}
