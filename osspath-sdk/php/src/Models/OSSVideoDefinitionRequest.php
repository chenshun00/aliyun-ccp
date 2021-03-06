<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\CCP\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 获取视频分辨率列表.
 */
class OSSVideoDefinitionRequest extends Model
{
    /**
     * @description drive_id
     *
     * @example 1
     *
     * @var string
     */
    public $driveId;

    /**
     * @description file_path
     *
     * @example /a/b/c.mp4
     *
     * @var string
     */
    public $filePath;

    /**
     * @description protection_scheme
     *
     * @example cbcs
     *
     * @var string
     */
    public $protectionScheme;

    /**
     * @description share_id
     *
     * @example 3d336314-63c8-4d96-bce0-17aefb6833b6
     *
     * @var string
     */
    public $shareId;
    protected $_name = [
        'driveId'          => 'drive_id',
        'filePath'         => 'file_path',
        'protectionScheme' => 'protection_scheme',
        'shareId'          => 'share_id',
    ];
    protected $_default = [
        'protectionScheme' => 'none',
    ];

    public function validate()
    {
        Model::validatePattern('driveId', $this->driveId, '[0-9]+');
        Model::validatePattern('shareId', $this->shareId, '[0-9a-zA-Z-]+');
        Model::validateRequired('filePath', $this->filePath, true);
        Model::validateMaxLength('filePath', $this->filePath, 1000);
        Model::validateMinLength('filePath', $this->filePath, 1);
    }

    public function toMap()
    {
        $res                      = [];
        $res['drive_id']          = $this->driveId;
        $res['file_path']         = $this->filePath;
        $res['protection_scheme'] = $this->protectionScheme;
        $res['share_id']          = $this->shareId;

        return $res;
    }

    /**
     * @param array $map
     *
     * @return OSSVideoDefinitionRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['drive_id'])) {
            $model->driveId = $map['drive_id'];
        }
        if (isset($map['file_path'])) {
            $model->filePath = $map['file_path'];
        }
        if (isset($map['protection_scheme'])) {
            $model->protectionScheme = $map['protection_scheme'];
        }
        if (isset($map['share_id'])) {
            $model->shareId = $map['share_id'];
        }

        return $model;
    }
}
