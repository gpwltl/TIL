//1. mymongo_db에서 사용
use mymongo_db
//2. order collection 생성
db.createCollection("orders")
//3. 데이터 insert
db.orders.insertMany([
{       cust_id: "abc123",
        ord_date: ISODate("2012-01-02T17:04:11.102Z"),
        status: 'A',
        price: 100,
        items: [ { sku: "xxx", qty: 25, price: 1 },
        { sku: "yyy", qty: 25, price: 1 } ]
},

{       cust_id: "abc123",
        ord_date: ISODate("2012-01-02T17:04:11.102Z"),
        status: 'A',
        price: 500,
        items: [ { sku: "xxx", qty: 25, price: 1 },
        { sku: "yyy", qty: 25, price: 1 } ]
},

{       cust_id: "abc123",
        ord_date: ISODate("2012-01-02T17:04:11.102Z"),
        status: 'B',
        price: 130,
        items: [ { sku: "jkl", qty: 35, price: 2 },
        { sku: "abv", qty: 35, price: 1 } ]
},

{       cust_id: "abc123",
        ord_date: ISODate("2012-01-02T17:04:11.102Z"),
        status: 'A',
        price: 130,
        items: [ { sku: "xxx", qty: 15, price: 1 },
        { sku: "yyy", qty: 15, price: 1 } ]
},

{       cust_id: "abc456",
        ord_date: ISODate("2012-02-02T17:04:11.102Z"),
        status: 'C',
        price: 70,
        items: [ { sku: "jkl", qty: 45, price: 2 },
        { sku: "abv", qty: 45, price: 3 } ]
},

{       cust_id: "abc456",
        ord_date: ISODate("2012-02-02T17:04:11.102Z"),
        status: 'A',
        price: 150,
        items: [ { sku: "xxx", qty: 35, price: 4 },
        { sku: "yyy", qty: 35, price: 5 } ]
},

{       cust_id: "abc456",
        ord_date: ISODate("2012-02-02T17:04:11.102Z"),
        status: 'B',
        price: 20,
        items: [ { sku: "jkl", qty: 45, price: 2 },
        { sku: "abv", qty: 45, price: 1 } ]
},

{       cust_id: "abc780",
        ord_date: ISODate("2012-02-02T17:04:11.102Z"),
        status: 'B',
        price: 260,
        items: [ { sku: "jkl", qty: 50, price: 2 },
        { sku: "abv", qty: 35, price: 1 } ]
}

])

//4. select count(*) as count from orders
db.orders.aggregate([
    {
        $group: {
        _id: null,
        count: {$sum: 1}
        }
    }
])

//5. select sum(price) as total from orders
db.orders.aggregate([
    {
        $group: {
            _id: null,
            total: {$sum: "$price"}
        }
    }
])

//6. select cust_id, sum(price) as total from orders group by cust_id
db.orders.aggregate([
    {
        $group: {
            _id: "$cust_id",
            total: {$sum: "$price"}
        }
    }
])

//7. select cust_id, ord_date, sum(price) as total from orders group by cust_id, ord_date
db.orders.aggregate([
    {
        $group: {
            _id: {
                cust_id: "$cust_id",
                ord_date: {$dateToString:{
                    format: "%Y-%m-%d",
                    date: "$ord_date"
                }}
            },
            total: {$sum: "$price"}
        }
    }
])

//8. select cust_id, count(*) from orders group by cust_id having count(*)>1
db.orders.aggregate([
    {
        $group: {
            _id: "$cust_id",
            count: {$sum: 1}
        }
    },
    {$match: {count: {$gt: 1}}}
])

//9. select cust_id, ord_date, sum(price) as total from orders group by cust_id, ord_date having total>250
db.orders.aggregate([
    {
        $group: {
            _id: {
                cust_id: "$cust_id",
                ord_date: {$dateToString:{
                    format: "%Y-%m-%d",
                    date: "$ord_date"
                }}
            },
            total: {$sum: "$price"}
        }
    },
    {$match: {total: {$gt: 250}}}
])

//10. select cust_id, sum(price) as total from orders where status='A' group by cust_id
db.orders.aggregate([
    {$match: {status:'A'}},
    {
        $group: {
            _id: "$cust_id",
            total: {$sum: "$price"}
        }
    }
])

//11. select cust_id, sum(price) as total from orders where status='A' group by cust_id having total>250
db.orders.aggregate([
    {$match: {status: 'A'}},
    {
        $group: {
            _id: "$cust_id",
            total: {$sum: "$price"}
        }
    },
    {$match: {total: {$gt: 250}}}
])

//12. select cust_id, sum(li.qty) as qty from orders o order_lineitem li where li.order_id=o.id group by cust_id
db.orders.aggregate([
    {$unwind: "$items"},
    {
        $group: {
            _id: "$cust_id",
            qty: {$sum: "$items.qty"}
        }
    }
])

//13. select count(*) from (select cust_id, ord_date from orders group by cust_id, ord_date) as DerivedTable
db.orders.aggregate([
    {
        $group: {
            _id: {
                cust_id: "$cust_id",
                ord_date: {$dateToString: {
                    format: "%Y-%m-%d",
                    date: "$ord_date"
                }}
            }
        }
    },
    {
        $group: {
            _id: null,
            count: {$sum: 1}
        }
    }
])