<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\CCP\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 全量获取file元信息的请求body.
 */
class CCPScanFileMetaRequest extends Model
{
    /**
     * @description category
     *
     * @example image
     *
     * @var string
     */
    public $category;

    /**
     * @description drive_id
     *
     * @example 1
     *
     * @var string
     */
    public $driveId;

    /**
     * @description limit
     *
     * @example 1000
     *
     * @var int
     */
    public $limit;

    /**
     * @description marker
     *
     * @example NWQ1Yjk4YmI1ZDRlYmU1Y2E0YWE0NmJhYWJmODBhNDQ2NzhlMTRhMg
     *
     * @var string
     */
    public $marker;
    protected $_name = [
        'category' => 'category',
        'driveId'  => 'drive_id',
        'limit'    => 'limit',
        'marker'   => 'marker',
    ];

    public function validate()
    {
        Model::validateRequired('driveId', $this->driveId, true);
        Model::validatePattern('driveId', $this->driveId, '[0-9]+');
        Model::validateMaximum('limit', $this->limit, 5000);
        Model::validateMinimum('limit', $this->limit, 1);
    }

    public function toMap()
    {
        $res             = [];
        $res['category'] = $this->category;
        $res['drive_id'] = $this->driveId;
        $res['limit']    = $this->limit;
        $res['marker']   = $this->marker;

        return $res;
    }

    /**
     * @param array $map
     *
     * @return CCPScanFileMetaRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['category'])) {
            $model->category = $map['category'];
        }
        if (isset($map['drive_id'])) {
            $model->driveId = $map['drive_id'];
        }
        if (isset($map['limit'])) {
            $model->limit = $map['limit'];
        }
        if (isset($map['marker'])) {
            $model->marker = $map['marker'];
        }

        return $model;
    }
}
