// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ccp.ossclient.models;

import com.aliyun.tea.*;

/**
 * 更新文件元数据
 */
public class CCPUpdateFileMetaRequest extends TeaModel {
    @NameInMap("custom_index_key")
    public String customIndexKey;

    @NameInMap("description")
    public String description;

    @NameInMap("drive_id")
    @Validation(required = true, pattern = "[0-9]+")
    public String driveId;

    @NameInMap("encrypt_mode")
    public String encryptMode;

    @NameInMap("file_id")
    @Validation(required = true, pattern = "[a-z0-9.-_]{1,50}")
    public String fileId;

    @NameInMap("hidden")
    public Boolean hidden;

    @NameInMap("labels")
    public java.util.List<String> labels;

    @NameInMap("meta")
    public String meta;

    @NameInMap("name")
    public String name;

    @NameInMap("starred")
    public Boolean starred;

    @NameInMap("user_meta")
    public String userMeta;

    public static CCPUpdateFileMetaRequest build(java.util.Map<String, ?> map) throws Exception {
        CCPUpdateFileMetaRequest self = new CCPUpdateFileMetaRequest();
        return TeaModel.build(map, self);
    }

}
