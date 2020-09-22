(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-2d0e95c4"], {
        "8ccf": function (e, t, a) {
            "use strict";
            a.r(t);
            var l = function () {
                    var e = this,
                        t = e.$createElement,
                        a = e._self._c || t;
                    return a("div", [a("el-table", {
                        directives: [{
                            name: "loading",
                            rawName: "v-loading",
                            value: e.loading,
                            expression: "loading"
                        }],
                        staticStyle: {
                            width: "100%"
                        },
                        attrs: {
                            data: e.saleInfo,
                            "max-height": "400"
                        }
                    }, [a("el-table-column", {
                        attrs: {
                            fixed: "",
                            prop: "totalnumber",
                            label: "已售出总数量",
                            width: "120"
                        }
                    })], 1), a("el-table", {
                        directives: [{
                            name: "loading",
                            rawName: "v-loading",
                            value: e.loading,
                            expression: "loading"
                        }],
                        staticStyle: {
                            width: "100%"
                        },
                        attrs: {
                            data: e.tableData,
                            "max-height": "400"
                        }
                    }, [a("el-table-column", {
                        attrs: {
                            fixed: "",
                            prop: "carnumber",
                            label: "汽车编号",
                            width: "120"
                        }
                    }), a("el-table-column", {
                        attrs: {
                            prop: "type",
                            label: "类型",
                            width: "120"
                        }
                    }), a("el-table-column", {
                        attrs: {
                            prop: "brand",
                            label: "品牌",
                            width: "120"
                        }
                    }), a("el-table-column", {
                        attrs: {
                            prop: "color",
                            label: "颜色",
                            width: "120"
                        }
                    }), a("el-table-column", {
                        attrs: {
                            prop: "price",
                            label: "价格",
                            width: "120"
                        }
                    }), a("el-table-column", {
                        attrs: {
                            prop: "entrydate",
                            label: "出厂日期",
                            width: "150"
                        }
                    }), a("el-table-column", {
                        attrs: {
                            prop: "saledate",
                            label: "售出日期",
                            width: "150"
                        }
                    })], 1)], 1)
                },
                n = [],
                o = a("cebe"),
                s = a.n(o),
                i = {
                    data: function () {
                        return {
                            tableData: [],
                            loading: !0,
                            saleInfo: []
                        }
                    },
                    mounted: function () {
                        this.getData()
                    },
                    methods: {
                        getData: function () {
                            var e = this,
                                t = "http://IP:5000/getinfo";
                            s.a.post(t, JSON.stringify({
                                gettype: 1
                            }), {
                                headers: {
                                    "Content-Type": "application/x-www-form-urlencoded",
                                    Accept: "application/json"
                                }
                            }).then((function (t) {
                                if (200 === t.data.code)
                                    if (0 === t.data.length) e.$message({
                                        showClose: !0,
                                        message: "暂无信息",
                                        type: "info"
                                    });
                                    else {
                                        e.tableData = t.data.items;
                                        var a = {
                                            totalnumber: t.data.items.length
                                        };
                                        e.saleInfo.push(a)
                                    }
                                else e.$message({
                                    showClose: !0,
                                    message: t.data.message,
                                    type: "error"
                                });
                                e.loading = !1
                            })).catch((function (t) {
                                e.$message({
                                    showClose: !0,
                                    message: t,
                                    type: "error"
                                })
                            }))
                        }
                    }
                },
                r = i,
                d = a("2877"),
                c = Object(d["a"])(r, l, n, !1, null, null, null);
            t["default"] = c.exports
        }
    }
]);