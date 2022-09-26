package org.example.scaffold.base.response;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

@ApiModel(description = "响应对象")
public class BaseApiResponse<T> {
    private static final int SUCCESS_CODE = 0;
    private static final String SUCCESS_MESSAGE = "成功";

    @ApiModelProperty(value = "响应码", name = "code", required = true, example = "" + SUCCESS_CODE)
    private int code;

    @ApiModelProperty(value = "响应消息", name = "msg", required = true, example = SUCCESS_MESSAGE)
    private String msg;

    @ApiModelProperty(value = "响应数据", name = "data")
    private T data;

    private BaseApiResponse(int code, String msg, T data) {
        this.code = code;
        this.msg = msg;
        this.data = data;
    }

    private BaseApiResponse() {
        this(SUCCESS_CODE, SUCCESS_MESSAGE);
    }

    private BaseApiResponse(int code, String msg) {
        this(code, msg, null);
    }

    private BaseApiResponse(T data) {
        this(SUCCESS_CODE, SUCCESS_MESSAGE, data);
    }

    public static <T> BaseApiResponse<T> success() {
        return new BaseApiResponse<>();
    }

    public static <T> BaseApiResponse<T> successWithData(T data) {
        return new BaseApiResponse<>(data);
    }

    public static <T> BaseApiResponse<T> failWithCodeAndMsg(int code, String msg) {
        return new BaseApiResponse<>(code, msg, null);
    }

    public static <T> BaseApiResponse<T> buildWithParam(ResponseParam param) {
        return new BaseApiResponse<>(param.getCode(), param.getMsg(), null);
    }

    public int getCode() {
        return code;
    }

    public void setCode(int code) {
        this.code = code;
    }

    public String getMsg() {
        return msg;
    }

    public void setMsg(String msg) {
        this.msg = msg;
    }

    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }


    public static class ResponseParam {
        private int code;
        private String msg;

        private ResponseParam(int code, String msg) {
            this.code = code;
            this.msg = msg;
        }

        public static ResponseParam buildParam(int code, String msg) {
            return new ResponseParam(code, msg);
        }

        public int getCode() {
            return code;
        }

        public void setCode(int code) {
            this.code = code;
        }

        public String getMsg() {
            return msg;
        }

        public void setMsg(String msg) {
            this.msg = msg;
        }
    }
}
