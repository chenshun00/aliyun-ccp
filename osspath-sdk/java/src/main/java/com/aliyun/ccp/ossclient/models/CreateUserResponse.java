// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.ccp.ossclient.models;

import com.aliyun.tea.*;

/**
 * Create user response
 */
public class CreateUserResponse extends TeaModel {
    @NameInMap("avatar")
    public String avatar;

    @NameInMap("created_at")
    public Long createdAt;

    @NameInMap("default_drive_id")
    public String defaultDriveId;

    @NameInMap("description")
    public String description;

    @NameInMap("domain_id")
    public String domainId;

    @NameInMap("email")
    public String email;

    @NameInMap("nick_name")
    public String nickName;

    @NameInMap("phone")
    public String phone;

    @NameInMap("role")
    public String role;

    @NameInMap("status")
    public String status;

    @NameInMap("updated_at")
    public Long updatedAt;

    @NameInMap("user_data")
    public java.util.Map<String, ?> userData;

    @NameInMap("user_id")
    public String userId;

    @NameInMap("user_name")
    public String userName;

    public static CreateUserResponse build(java.util.Map<String, ?> map) throws Exception {
        CreateUserResponse self = new CreateUserResponse();
        return TeaModel.build(map, self);
    }

}
