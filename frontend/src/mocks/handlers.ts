import { rest } from "msw";

export const handlers = [
  rest.get("/api/cards/", (_req, res, ctx) => {
    const data = [
      {
        id: 1,
        name: "皿洗い",
        point: 100,
        targets: [1, 2],
      },
      {
        id: 2,
        name: "勉強",
        point: 200,
        targets: [1],
      },
      {
        id: 3,
        name: "お風呂掃除",
        point: 300,
        targets: [2],
      },
    ];

    return res(
      ctx.status(200),

      ctx.json(data)
    );
  }),
  rest.get("/api/members/", (_req, res, ctx) => {
    return res(
      ctx.status(200),
      ctx.json([
        { id: 1, name: "太郎", point: 1000 },
        { id: 2, name: "花子", point: 500 },
      ])
    );
  }),
  rest.get("/api/cards/new/", (_req, res, ctx) => {
    return res(ctx.status(200), ctx.json({ id: 5, name: "", point: 0 }));
  }),
];
