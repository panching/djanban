import { CountPipe } from './pipes/count.pipe';
import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';

import { HttpModule }    from '@angular/http';

import { AppComponent }  from './app.component';


import { AppRoutingModule } from './app-routing.module';
import { BoardService } from '../services/board.service';
import { BoardComponent } from '../components/board/board.component';
import { DashboardComponent } from '../components/dashboard/dashboard.component';
import { CardComponent } from '../components/card/card.component';
import { CardService } from '../services/card.service';
import { MemberService } from '../services/member.service';


import { DragulaModule } from 'ng2-dragula/ng2-dragula';
import { FileUploadModule } from 'ng2-file-upload';
import { SimpleNotificationsModule, NotificationsService } from 'angular2-notifications';
import { LocalizeDatetimePipe } from './pipes/localize_datetime.pipe';
import { ActiveCardsPipe } from './pipes/active_cards.pipe';
import { SelectModule } from 'angular2-select';

@NgModule({
  imports: [ 
    BrowserModule,
    HttpModule,
    FormsModule, 
    AppRoutingModule,
    DragulaModule,
    FileUploadModule,
    SelectModule,
    SimpleNotificationsModule.forRoot()
  ],
  declarations: [
    AppComponent,
    LocalizeDatetimePipe, ActiveCardsPipe, CountPipe,
    DashboardComponent, BoardComponent, CardComponent
  ],
  providers: [ MemberService, BoardService, CardService, NotificationsService ],
  bootstrap:    [ AppComponent ]
})

export class AppModule {

}
