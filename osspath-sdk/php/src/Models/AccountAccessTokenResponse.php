<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\CCP\SDK\Models;

use AlibabaCloud\Tea\Model;

class AccountAccessTokenResponse extends Model
{
    /**
     * @description 用于调用业务接口的accessToken
     *
     * @example cnskjajkahwdhwialsnd
     *
     * @var string
     */
    public $accessToken;

    /**
     * @description 当前用户头像
     *
     * @example cherry
     *
     * @var string
     */
    public $avatar;

    /**
     * @description 用户的数据密码是否保存服务端
     *
     * @example true
     *
     * @var bool
     */
    public $dataPinSaved;

    /**
     * @description 用户的数据密码是否设置过
     *
     * @example true
     *
     * @var bool
     */
    public $dataPinSetup;

    /**
     * @description Default Drive ID
     *
     * @example 100
     *
     * @var string
     */
    public $defaultDriveId;

    /**
     * @description 当前用户已存在的登录方式
     *
     * @example
     *
     * @var array
     */
    public $existLink;

    /**
     * @description accessToken过期时间，ISO时间
     *
     * @example 2019-09-01T06:57:48.813Z
     *
     * @var string
     */
    public $expireTime;

    /**
     * @description accessToken过期时间，单位秒
     *
     * @example 3600
     *
     * @var int
     */
    public $expiresIn;

    /**
     * @description 用户是否为第一次登录
     *
     * @example true
     *
     * @var bool
     */
    public $isFirstLogin;

    /**
     * @description 是否需要绑定
     *
     * @example false
     *
     * @var bool
     */
    public $needLink;

    /**
     * @description 当前用户昵称
     *
     * @example cherry
     *
     * @var string
     */
    public $nickName;

    /**
     * @description 用于刷新accessToken
     *
     * @example cnskjajkahwdhwialsnd
     *
     * @var string
     */
    public $refreshToken;

    /**
     * @description 当前用户角色
     *
     * @example user
     *
     * @var string
     */
    public $role;

    /**
     * @description 临时权限，用于登录成功后设置密码
     *
     * @example klafhjas-asdasd-asd-as-d-asd-asd-asdasd
     *
     * @var string
     */
    public $state;

    /**
     * @description accessToken类型，Bearer
     *
     * @example Bearer
     *
     * @var string
     */
    public $tokenType;

    /**
     * @description 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
     *
     * @example { is_student: true }
     *
     * @var object
     */
    public $userData;

    /**
     * @description 当前用户ID
     *
     * @example DING-xxxxx
     *
     * @var string
     */
    public $userId;

    /**
     * @description 当前用户名
     *
     * @example cherry
     *
     * @var string
     */
    public $userName;
    protected $_name = [
        'accessToken'    => 'access_token',
        'avatar'         => 'avatar',
        'dataPinSaved'   => 'data_pin_saved',
        'dataPinSetup'   => 'data_pin_setup',
        'defaultDriveId' => 'default_drive_id',
        'existLink'      => 'exist_link',
        'expireTime'     => 'expire_time',
        'expiresIn'      => 'expires_in',
        'isFirstLogin'   => 'is_first_login',
        'needLink'       => 'need_link',
        'nickName'       => 'nick_name',
        'refreshToken'   => 'refresh_token',
        'role'           => 'role',
        'state'          => 'state',
        'tokenType'      => 'token_type',
        'userData'       => 'user_data',
        'userId'         => 'user_id',
        'userName'       => 'user_name',
    ];

    public function validate()
    {
        Model::validateRequired('accessToken', $this->accessToken, true);
        Model::validateRequired('needLink', $this->needLink, true);
    }

    public function toMap()
    {
        $res                     = [];
        $res['access_token']     = $this->accessToken;
        $res['avatar']           = $this->avatar;
        $res['data_pin_saved']   = $this->dataPinSaved;
        $res['data_pin_setup']   = $this->dataPinSetup;
        $res['default_drive_id'] = $this->defaultDriveId;
        $res['exist_link']       = [];
        if (null !== $this->existLink && \is_array($this->existLink)) {
            $n = 0;
            foreach ($this->existLink as $item) {
                $res['exist_link'][$n++] = null !== $item ? $item->toMap() : $item;
            }
        }
        $res['expire_time']    = $this->expireTime;
        $res['expires_in']     = $this->expiresIn;
        $res['is_first_login'] = $this->isFirstLogin;
        $res['need_link']      = $this->needLink;
        $res['nick_name']      = $this->nickName;
        $res['refresh_token']  = $this->refreshToken;
        $res['role']           = $this->role;
        $res['state']          = $this->state;
        $res['token_type']     = $this->tokenType;
        $res['user_data']      = $this->userData;
        $res['user_id']        = $this->userId;
        $res['user_name']      = $this->userName;

        return $res;
    }

    /**
     * @param array $map
     *
     * @return AccountAccessTokenResponse
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['access_token'])) {
            $model->accessToken = $map['access_token'];
        }
        if (isset($map['avatar'])) {
            $model->avatar = $map['avatar'];
        }
        if (isset($map['data_pin_saved'])) {
            $model->dataPinSaved = $map['data_pin_saved'];
        }
        if (isset($map['data_pin_setup'])) {
            $model->dataPinSetup = $map['data_pin_setup'];
        }
        if (isset($map['default_drive_id'])) {
            $model->defaultDriveId = $map['default_drive_id'];
        }
        if (isset($map['exist_link'])) {
            if (!empty($map['exist_link'])) {
                $model->existLink = [];
                $n                = 0;
                foreach ($map['exist_link'] as $item) {
                    $model->existLink[$n++] = null !== $item ? LinkInfo::fromMap($item) : $item;
                }
            }
        }
        if (isset($map['expire_time'])) {
            $model->expireTime = $map['expire_time'];
        }
        if (isset($map['expires_in'])) {
            $model->expiresIn = $map['expires_in'];
        }
        if (isset($map['is_first_login'])) {
            $model->isFirstLogin = $map['is_first_login'];
        }
        if (isset($map['need_link'])) {
            $model->needLink = $map['need_link'];
        }
        if (isset($map['nick_name'])) {
            $model->nickName = $map['nick_name'];
        }
        if (isset($map['refresh_token'])) {
            $model->refreshToken = $map['refresh_token'];
        }
        if (isset($map['role'])) {
            $model->role = $map['role'];
        }
        if (isset($map['state'])) {
            $model->state = $map['state'];
        }
        if (isset($map['token_type'])) {
            $model->tokenType = $map['token_type'];
        }
        if (isset($map['user_data'])) {
            $model->userData = $map['user_data'];
        }
        if (isset($map['user_id'])) {
            $model->userId = $map['user_id'];
        }
        if (isset($map['user_name'])) {
            $model->userName = $map['user_name'];
        }

        return $model;
    }
}
