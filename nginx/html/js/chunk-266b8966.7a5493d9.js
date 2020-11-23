(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-266b8966"], {
        "0f66": function (t, a, e) {},
        "7c78": function (t, a, e) {
            "use strict";
            e.r(a);
            var o = function () {
                    var t = this,
                        a = t.$createElement,
                        e = t._self._c || a;
                    return e("d2-container", [e("template", {
                        slot: "header"
                    }, [t._v("汽车类型销售统计")]), e("div", {
                        staticClass: "inner"
                    }, [e("ve-pie", t._b({
                        attrs: {
                            data: t.chartData
                        }
                    }, "ve-pie", t.pubSetting, !1))], 1)], 2)
                },
                n = [],
                s = e("cebe"),
                r = e.n(s),
                i = e("7923"),
                c = {
                    mixins: [i["default"]],
                    data: function () {
                        return {
                            chartData: {
                                columns: ["type", "froportion"],
                                rows: [{
                                    type: "家用轿车",
                                    froportion: 0
                                }, {
                                    type: "SUV",
                                    froportion: 0
                                }, {
                                    type: "越野车",
                                    froportion: 0
                                }]
                            }
                        }
                    },
                    mounted: function () {
                        this.getData()
                    },
                    methods: {
                        getData: function () {
                            var t = this,
                                a = "http://IP:5000/type";
                            r.a.post(a).then((function (a) {
                                200 === a.data.code ? 0 === a.data.length ? t.$message({
                                    showClose: !0,
                                    message: "暂无信息",
                                    type: "info"
                                }) : (t.chartData.rows[0].froportion = a.data.saloon, t.chartData.rows[1].froportion = a.data.suv, t.chartData.rows[2].froportion = a.data.cross) : t.$message({
                                    showClose: !0,
                                    message: a.data.message,
                                    type: "error"
                                }), t.loading = !1
                            })).catch((function (a) {
                                t.$message({
                                    showClose: !0,
                                    message: a,
                                    type: "error"
                                })
                            }))
                        }
                    }
                },
                p = c,
                f = (e("85f5"), e("2877")),
                u = Object(f["a"])(p, o, n, !1, null, "388e05d6", null);
            a["default"] = u.exports
        },
        "85f5": function (t, a, e) {
            "use strict";
            var o = e("0f66"),
                n = e.n(o);
            n.a
        }
    }
]);