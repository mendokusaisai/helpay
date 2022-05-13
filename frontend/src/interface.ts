export interface Card {
  id: number;
  name: string;
  point: number;
  targets: Array<Member>;
}

export interface Member {
  id: number;
  name: string;
  point: number;
}
