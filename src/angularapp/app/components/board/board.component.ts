import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Board } from '../../models/board';
import { BoardService } from '../../services/board.service';
import { ActivatedRoute } from '@angular/router';
import { Card } from '../../models/card';
import {DragulaDirective, DragulaService} from 'ng2-dragula/ng2-dragula';
import { List } from '../../models/list';
import { CardService } from '../../services/card.service';
import { Member } from '../../models/member';
import { MemberService } from '../../services/member.service';


@Component({
    moduleId: module.id,
    selector: 'board',
    templateUrl: 'board.component.html',
    styleUrls: ['board.component.css'],
    providers: [MemberService, BoardService, CardService, DragulaService]
})

export class BoardComponent implements OnInit {
    board: Board;
    members: Member[];
    showNewCardForm: {};
    showAddMemberForm?: boolean;

    ngOnInit(): void {
      let that = this;
      this.route.params.subscribe(params => {
        let board_id = params["board_id"];
        that.loadBoard(board_id);
      });
      this.loadMembers();
    }

      constructor(
        private router: Router,
        private route: ActivatedRoute,
        private memberService: MemberService,
        private boardService: BoardService,
        private cardService: CardService,
        private dragulaService: DragulaService
    ) {
      this.showNewCardForm = { };

      dragulaService.setOptions('lists', {
        moves: function (el: any, container: any, handle: any) {
          return handle.className === 'move_list_handle';
        }
      });
      
      dragulaService.drop.subscribe((parameters: any) => {
        // Card drop
        if(parameters[0] == "cards"){
          this.onCardDrop(parameters);
        }else if(parameters[0] == "lists"){
          this.onListDrop(parameters);
        }
        
      });
    }

    private onCardDrop(parameters: any) {
      
      // Source list
      let source_list_id = parameters[3]["dataset"]["list"];
      let source_list = new List(this.board.getListById(parseInt(source_list_id)));
      
      // Destination list
      let destination_list_id = parameters[2]["dataset"]["list"];
      let destination_list = new List(this.board.getListById(parseInt(destination_list_id)));

      // Card that has bee moved from source list to destination list
      let moved_card_id = parameters[1]["dataset"]["card"];
      let moved_card = destination_list.getCardById(parseInt(moved_card_id));

      // Next card in order in destination
      let next_card_in_destination_id = null;
      // If next card is null, the moved card is the last one of the list
      let next_card = null;
      if(parameters[4] != null){
        next_card_in_destination_id = parameters[4]["dataset"]["card"];
        next_card = destination_list.getCardById(parseInt(next_card_in_destination_id));
      }

      let destination_position = "bottom";
      if (next_card != null){
        destination_position = (next_card.position - 10).toString();
      }

      // Move card to list
      this.cardService.moveCard(moved_card, destination_list, destination_position).then(card => {
        //source_list.removeCard(moved_card);
        //destination_list.addCard(moved_card, destination_position);
      });
    }

    private onListDrop(parameters: any) {
      // Moved list
      let moved_list_id = parameters[1]["dataset"]["list"];
      let moved_list = new List(this.board.getListById(parseInt(moved_list_id)));

      // Next list after the list has been moved
      let next_list_id = parameters[4]["dataset"]["list"];
      let next_list = null;
      let destination_position = "bottom";
      if(next_list_id){
        next_list = new List(this.board.getListById(parseInt(next_list_id)));
        destination_position = (next_list.position - 10).toString();
      }

      this.boardService.moveList(this.board, moved_list, destination_position).then(list => { moved_list.position = list.position; });
      
    }

    /** Load board */
    loadBoard(board_id: number): void {
        this.boardService.getBoard(board_id).then(board_response =>{
          this.board = new Board(board_response);
        });
    }

    /** Load all available members */
    loadMembers(): void {
      this.memberService.getMembers().then(members => this.members = members);
    }

    /** Move to the card view */
    onCardSelect(card: Card): void {
      this.router.navigate([this.board.id, 'card', card.id]);
    }

    /* Controls for card creation form */
    onNewCardSubmit(list: List, name: string, position: string): void {
      this.cardService.addCard(this.board, list, name, position).then(card_response => {
        List.addCardToList(list, card_response, position);
        this.showNewCardForm[list.id] = false;
      });
    }

    /* Member actions */
    removeMember(member: Member): void {
      this.boardService.removeMember(this.board, member).then(deleted_member => {
        this.board.removeMember(member);
      });
    }

    onAddMemberSubmit(member_id: number):void {
      let member = this.members.find(function(member_i: Member){ return member_i.id == member_id; });
      if(member){
        this.boardService.addMember(this.board, member).then(added_member => {
          this.board.addMember(added_member);
          this.showAddMemberForm = false;
        });
      }
    }

}