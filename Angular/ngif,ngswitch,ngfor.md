# Angular View

```tsx
import { Component } from '@angular/core';
 
@Component({
  selector: 'app-test1',
  templateUrl: './test1.component.html',
  styleUrls: ['./test1.component.css']
})
export class Test1Component {
  inputName: string = "mango";
  fruits: string[] = ['jamong','mango','grape'];
}
```



## :dizzy: ngIf

- 단독으로 사용이 가능
- else나 then else를 같이 사용하는 방법도 존대

```html
<mat-form-field>
    <input matInput type="text" placeholder="입력하세요.." [(ngModel)]="inputName">
</mat-form-field>
 
<p *ngIf="inputName == 'jamong'">{{inputName}}을 입력하였습니다.</p>
```

-> **조건이 부합하는 경우에만 p태그가 화면에 보여질 것**

(현재 inputName이 'mango'이기 때문에 화면에는 아무것도 보이지 않을 것.)

```html
<mat-form-field>
    <input matInput type="text" placeholder="입력하세요.." [(ngModel)]="inputName">
</mat-form-field>
 
<p *ngIf="inputName == 'jamong'; then thenResult; else otherResult">{{inputName}}을 입력하였습니다.</p>
 
<ng-template #thenResult>
  <p>{{inputName}} 입니다.</p>
</ng-template>
 
<ng-template #otherResult>
  <p>jamong이 아니고 {{inputName}} 입니다.</p>
</ng-template>
```

-> ngIf 조건 뒤에 then else를 이용해 inputName이 jamong이라면, #thenResult 템플릿을 출력하고, 아닌 경우 #otherResult 템플릿을 출력.

-> ngIf조건이 붙여진 p태그 안의 내용은 무시됨

(inputName이 'mango'이기에, 화면에는 #otherResult 템플릿을 적용한 내용이 출력될 것.)





## :dizzy: ngSwitch

- ngSwitchCase, ngSwitchDefault 속성 사용

```html
<mat-form-field>
    <input matInput type="text" placeholder="입력하세요.." [(ngModel)]="inputName">
</mat-form-field>
 
<ul [ngSwitch]='inputName'>
  <li *ngSwitchCase="'jamong'">{{inputName}}은 3000원이에요</li>
  <li *ngSwitchCase="'mango'">{{inputName}}은 4000원이에요</li>
  <li *ngSwitchCase="'grape'">{{inputName}}은 5000원이에요</li>
  <li *ngSwitchDefault>{{inputName}}은 팔지 않아요</li>
</ul>
```

(inputName이 'mango'이기에, 화면에는 "**mango은 4000원이에요**"을 출력하게 됨.)





## :dizzy: ngFor

- 반복문을 사용하여 table이나 list를 출력해주는 작업 가능
- object를 이용한 반복만 가능
- 횟수 반복을 하기 위해서 배열에다 숫자를 넣어서 작업해야 함

```html
<ul>
  <li *ngFor='let fruit of fruits'>
    {{fruit}}
  </li>
</ul>
```

(jamong, mango, grape 순으로 출력)

<br/>

> **ngFor과 ngIf를 동시에 사용하고 싶다면 ?**

```html
<ul>
  <li *ngFor="let fruit of fruits">
    <span *ngIf="fruit == 'jamong' || fruit == 'grape'">{{ fruit }}</span>
  </li>
</ul>

```

(jamong과 grape만 조건에 맞기 때문에 둘만 출력됨)

> **태그를 사용하지 않고 ng-container 사용하는 방법**

```html
<ul>
  <li *ngFor="let fruit of fruits">
    <ng-container *ngIf="fruit != 'jamong'">{{ fruit }}</ng-container>
  </li>
</ul>
```

