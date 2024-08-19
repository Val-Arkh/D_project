select c.login, count(o) from "Couriers" AS c INNER JOIN "Orders" as o on c.id=o."courierId" WHERE o."inDelivery" = true group by (c.login);
