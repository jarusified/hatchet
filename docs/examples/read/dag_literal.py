#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import hatchet as ht


if __name__ == "__main__":
    # Define a literal GraphFrame using a list of dicts.
    gf = ht.GraphFrame.from_literal(
        [
            {
                "name": "foo",
                "type": "function",
                "metrics": {"time (inc)": 130.0, "time": 0.0},
                "children": [
                    {
                        "name": "bar",
                        "type": "function",
                        "metrics": {"time (inc)": 20.0, "time": 5.0},
                        "children": [
                            {
                                "name": "baz",
                                "type": "function",
                                "metrics": {"time (inc)": 5.0, "time": 5.0},
                            },
                            {
                                "name": "grault",
                                "type": "function",
                                "metrics": {"time (inc)": 10.0, "time": 10.0},
                            },
                        ],
                    },
                    {
                        "name": "qux",
                        "type": "function",
                        "metrics": {"time (inc)": 60.0, "time": 0.0},
                        "children": [
                            {
                                "name": "quux",
                                "type": "function",
                                "metrics": {"time (inc)": 60.0, "time": 5.0},
                                "children": [
                                    {
                                        "name": "corge",
                                        "type": "function",
                                        "metrics": {"time (inc)": 55.0, "time": 10.0},
                                        "children": [
                                            {
                                                "name": "bar",
                                                "type": "function",
                                                "metrics": {
                                                    "time (inc)": 20.0,
                                                    "time": 5.0,
                                                },
                                                "children": [
                                                    {
                                                        "name": "baz",
                                                        "type": "function",
                                                        "metrics": {
                                                            "time (inc)": 5.0,
                                                            "time": 5.0,
                                                        },
                                                    },
                                                    {
                                                        "name": "grault",
                                                        "type": "function",
                                                        "metrics": {
                                                            "time (inc)": 10.0,
                                                            "time": 10.0,
                                                        },
                                                    },
                                                ],
                                            },
                                            {
                                                "name": "grault",
                                                "type": "function",
                                                "metrics": {
                                                    "time (inc)": 10.0,
                                                    "time": 10.0,
                                                },
                                            },
                                            {
                                                "name": "garply",
                                                "type": "function",
                                                "metrics": {
                                                    "time (inc)": 15.0,
                                                    "time": 15.0,
                                                },
                                            },
                                        ],
                                    }
                                ],
                            }
                        ],
                    },
                    {
                        "name": "waldo",
                        "type": "function",
                        "metrics": {"time (inc)": 50.0, "time": 0.0},
                        "children": [
                            {
                                "name": "fred",
                                "type": "function",
                                "metrics": {"time (inc)": 35.0, "time": 5.0},
                                "children": [
                                    {
                                        "name": "plugh",
                                        "type": "function",
                                        "metrics": {"time (inc)": 5.0, "time": 5.0},
                                    },
                                    {
                                        "name": "xyzzy",
                                        "type": "function",
                                        "metrics": {"time (inc)": 25.0, "time": 5.0},
                                        "children": [
                                            {
                                                "name": "thud",
                                                "type": "function",
                                                "metrics": {
                                                    "time (inc)": 25.0,
                                                    "time": 5.0,
                                                },
                                                "children": [
                                                    {
                                                        "name": "baz",
                                                        "type": "function",
                                                        "metrics": {
                                                            "time (inc)": 5.0,
                                                            "time": 5.0,
                                                        },
                                                    },
                                                    {
                                                        "name": "garply",
                                                        "type": "function",
                                                        "metrics": {
                                                            "time (inc)": 15.0,
                                                            "time": 15.0,
                                                        },
                                                    },
                                                ],
                                            }
                                        ],
                                    },
                                ],
                            },
                            {
                                "name": "garply",
                                "type": "function",
                                "metrics": {"time (inc)": 15.0, "time": 15.0},
                            },
                        ],
                    },
                ],
            },
            {
                "name": "ほげ (hoge)",
                "type": "function",
                "metrics": {"time (inc)": 30.0, "time": 0.0},
                "children": [
                    {
                        "name": "(ぴよ (piyo)",
                        "type": "function",
                        "metrics": {"time (inc)": 15.0, "time": 5.0},
                        "children": [
                            {
                                "name": "ふが (fuga)",
                                "type": "function",
                                "metrics": {"time (inc)": 5.0, "time": 5.0},
                            },
                            {
                                "name": "ほげら (hogera)",
                                "type": "function",
                                "metrics": {"time (inc)": 5.0, "time": 5.0},
                            },
                        ],
                    },
                    {
                        "name": "ほげほげ (hogehoge)",
                        "type": "function",
                        "metrics": {"time (inc)": 15.0, "time": 15.0},
                    },
                ],
            },
        ]
    )

    # Printout the DataFrame component of the GraphFrame.
    print(gf.dataframe)

    # Printout the graph component of the GraphFrame.
    # Because no metric parameter is specified, ``time`` is used by default.
    print(gf.tree())
