// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.CCP.CCPClient.Models
{
    public class CopyFileRequest : TeaModel {
        [NameInMap("header")]
        [Validation(Required=false)]
        public CopyFileRequestHeader Header { get; set; }
        public class CopyFileRequestHeader : TeaModel {
            [NameInMap("x-pds-trace-id")]
            [Validation(Required=false)]
            public string TraceId { get; set; }
            [NameInMap("x-pds-device-id")]
            [Validation(Required=false)]
            public string DeviceId { get; set; }
        };

        [NameInMap("drive_id")]
        [Validation(Required=true, Pattern="[0-9]+")]
        public string DriveId { get; set; }

        [NameInMap("file_id")]
        [Validation(Required=true, MaxLength=50, Pattern="[a-z0-9.-_]{1,50}")]
        public string FileId { get; set; }

        [NameInMap("file_path")]
        [Validation(Required=false)]
        public string FilePath { get; set; }

        [NameInMap("new_name")]
        [Validation(Required=true, Pattern="[a-zA-Z0-9.-]{1,1000}")]
        public string NewName { get; set; }

        [NameInMap("overwrite")]
        [Validation(Required=false)]
        public bool? Overwrite { get; set; }

        [NameInMap("share_id")]
        [Validation(Required=false)]
        public string ShareId { get; set; }

        [NameInMap("to_drive_id")]
        [Validation(Required=true, Pattern="[0-9]+")]
        public string ToDriveId { get; set; }

        [NameInMap("to_parent_file_id")]
        [Validation(Required=true, MaxLength=50, Pattern="[a-z0-9.-_]{1,50}")]
        public string ToParentFileId { get; set; }

        [NameInMap("to_parent_file_path")]
        [Validation(Required=false)]
        public string ToParentFilePath { get; set; }

        [NameInMap("to_share_id")]
        [Validation(Required=false)]
        public string ToShareId { get; set; }

    }

}
